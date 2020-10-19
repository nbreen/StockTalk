import { Injectable } from '@angular/core';
import { User, Topic, Post, Comment, 
         PostVotes, CommentVotes, UserFollowsTopic, 
         UserFollowsUser, UserSavesPost, Profile } from './Interfaces';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { isPrivateIdentifier } from 'typescript';
import { Router } from '@angular/router';
 
@Injectable({
  providedIn: 'root'
})

export class CrudService {

  readonly APIUrl = "http://127.0.0.1:8000";
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  
  constructor(private httpClient: HttpClient, private router: Router) { }

  private instanceOfObj(object : any) {
    return object.Type;
  }

  getAll<T>(type : string): Observable<T[]> {

    return this.httpClient.get<T[]>(this.APIUrl + type)
    .pipe(map(res => []));
    
    /*
    .pipe(
      catchError(this.handleError<User>('getAllUsers'))
    )
    */
    
  }

  getUserProfile(username:string): Observable<Profile> {
    return this.httpClient.get(this.APIUrl + "/profiles/" + username)
      .pipe(map((data: {profile: Profile}) => data.profile));
  }

  addUser(toAdd: User) {

      let body = JSON.stringify(toAdd);
      return this.httpClient.post<User>(this.APIUrl + "/user/", body);

      /*
      .pipe(
        catchError(this.handleError<User>('createUser'))
      );
      */
  }

  getUserById<T>(id : Number, type : T) : Observable<T> {

    var typeStr = this.instanceOfObj(type);

    return this.httpClient.get<T>(this.APIUrl + typeStr + id, this.httpOptions);

    /*
    .pipe(
      catchError(this.handleError<User>('getUserById'))
    );
    */
  }

  

  updateUser<T>(id : Number, type : T, val : any): Observable<T> {

    var typeStr = this.instanceOfObj(type);

    return this.httpClient.put<T>(this.APIUrl + typeStr + id + JSON.stringify(val), this.httpOptions);

    /*
    .pipe(
      catchError(this.handleError<User>('updateUser'))
    );
    */

  }

  deleteUser<T>(id : Number, type : T): Observable<T> {

    var typeStr = this.instanceOfObj(type);

    return this.httpClient.delete<T>(this.APIUrl + typeStr + id, this.httpOptions);

    /*
    .pipe(
      catchError(this.handleError<User>('deleteUser'))
    )
    */
   
  }

  login(userName: String) {
    console.log("Input is", userName);
    this.httpClient.post(this.APIUrl, JSON.stringify(userName))
        .subscribe(result => {
          this.router.navigate(["/alltopics"], { "queryParams": result});
        })
  }

  /* need create read update delete for 
  
    Interation
    comment
    Post
    Topic
    User
  
  */

  /** Message service for loggin success of crud operations */
  /*private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */

  private handleError<T>(operation = 'operation', result?: T) {
      // TODO: send the error to remote logging infrastructure
      console.log(operation); // log to console instead
  };
}
