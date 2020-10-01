import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlltopicsComponent } from './alltopics.component';

describe('AlltopicsComponent', () => {
  let component: AlltopicsComponent;
  let fixture: ComponentFixture<AlltopicsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlltopicsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlltopicsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
