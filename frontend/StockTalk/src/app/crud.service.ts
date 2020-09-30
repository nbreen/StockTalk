import { Injectable } from '@angular/core';
import { User } from '../app/user';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
 
@Injectable({
  providedIn: 'root'
})

export class CrudService {

  private apiServer = "http://<address of our server>"

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  constructor(private httpClient: HttpClient) { }

  getAllUsers(): Observable<User> {
    return this.httpClient.get<User>(this.apiServer + "path")
    
    /*
    .pipe(
      catchError(this.handleError<User>('getAllUsers'))
    )
    */
    
  }

  createUser(user): Observable<User> {
      return this.httpClient.post<User>(this.apiServer + "path", JSON.stringify(user), this.httpOptions)

      /*
      .pipe(
        catchError(this.handleError<User>('createUser'))
      );
      */
  }

  getUserById(id) : Observable<User> {
    return this.httpClient.get<User>(this.apiServer + "path")

    /*
    .pipe(
      catchError(this.handleError<User>('getUserById'))
    );
    */
  }

  updateUser(id, user): Observable<User> {
    return this.httpClient.put<User>(this.apiServer + "path", JSON.stringify(user), this.httpOptions)

    /*
    .pipe(
      catchError(this.handleError<User>('updateUser'))
    );
    */

  }

  deleteUser(id): Observable<User> {
    return this.httpClient.delete<User>(this.apiServer + "path", this.httpOptions)

    /*
    .pipe(
      catchError(this.handleError<User>('deleteUser'))
    )
    */
   
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
