import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Profile } from '../app/profile';
import { isPrivateIdentifier } from 'typescript';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private httpClient: HttpClient) { }

  readonly APIUrl = "http://127.0.0.1:8000";
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  get(username: string): Observable<Profile> {
    return this.httpClient.get(this.APIUrl + "/profiles/" + username)
      .pipe(map((data: {profile: Profile}) => data.profile));

  }
}
